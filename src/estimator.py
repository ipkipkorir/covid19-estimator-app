import math
def estimator(data):
		
	#Convert or check that 'timeToElapse' is in days
	if data['periodType'] == 'days':
		timeInDays = data['timeToElapse']
	elif data['periodType'] == 'weeks':
		timeInDays = data['timeToElapse'] * 7
	elif data['periodType'] == 'months':
		timeInDays = data['timeToElapse'] * 30

	#Compute estimates:
	##Impact computation
	impactCurrentlyInfected = data['reportedCases'] * 10
	impactInfectionsByRequestedTime = impactCurrentlyInfected * (2 ** (timeInDays // 3))
	impactSevereCasesByRequestedTime = (0.15 * impactInfectionsByRequestedTime) // 1
	impactHospitalBedsByRequestedTime = (((0.35 * data['totalHospitalBeds']) * timeInDays) - impactSevereCasesByRequestedTime) // 1
	impactCasesForICUByRequestedTime = (0.05 * impactInfectionsByRequestedTime) // 1
	impactCasesForVentilatorsByRequestedTime = (0.02 * impactInfectionsByRequestedTime) // 1
	impactDollarsInFlight = (((impactInfectionsByRequestedTime * data["region"]['avgDailyIncomePopulation']) * data["region"]['avgDailyIncomeInUSD']) // timeInDays) // 1

	#Compute estimates:
	##Severe Impact computation
	severeImpactCurrentlyInfected = data['reportedCases'] * 50
	severeImpactInfectionsByRequestedTime = severeImpactCurrentlyInfected * (2 ** (timeInDays // 3))
	severeImpactSevereCasesByRequestedTime =  (0.15 * severeImpactInfectionsByRequestedTime) // 1
	severeImpactHospitalBedsByRequestedTime = (((0.35 * data['totalHospitalBeds']) * timeInDays)- severeImpactSevereCasesByRequestedTime) // 1
	severeImpactCasesForICUByRequestedTime = (0.05 * severeImpactInfectionsByRequestedTime) // 1
	severeImpactCasesForVentilatorsByRequestedTime = (0.02 * severeImpactInfectionsByRequestedTime) // 1
	severeImpactDollarsInFlight = (((severeImpactInfectionsByRequestedTime * data["region"]['avgDailyIncomePopulation']) * data["region"]['avgDailyIncomeInUSD']) // timeInDays) // 1

	#Estimates
	estimate = {
		'data' : data,

		'impact' : {
			'currentlyInfected' : impactCurrentlyInfected,
			'infectionsByRequestedTime' : impactInfectionsByRequestedTime,
			'severeCasesByRequestedTime' : impactSevereCasesByRequestedTime,
			'HospitalBedsByRequestedTime' : impactHospitalBedsByRequestedTime,
			'casesForICUByRequestedTime' : impactCasesForICUByRequestedTime,
			'casesForVentilatorsByRequestedTime' : impactCasesForVentilatorsByRequestedTime,
			'dollarsInFlight' : impactDollarsInFlight
		},

		'severeImpact' : {
				'currentlyInfected' : severeImpactCurrentlyInfected,
				'infectionsByRequestedTime' :  severeImpactInfectionsByRequestedTime,
				'severeCasesByRequestedTime' : severeImpactSevereCasesByRequestedTime,
				'HospitalBedsByRequestedTime' : severeImpactHospitalBedsByRequestedTime,
				'casesForICUByRequestedTime' : severeImpactCasesForICUByRequestedTime,
				'casesForVentilatorsByRequestedTime' : severeImpactCasesForVentilatorsByRequestedTime,
				'dollarsInFlight' : severeImpactDollarsInFlight
		}

	}
	return estimate
