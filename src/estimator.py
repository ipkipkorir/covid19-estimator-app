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
	impactSevereCasesByRequestedTime = math.trunc(0.15 * impactInfectionsByRequestedTime)
	impactHospitalBedsByRequestedTime = math.trunc((0.35 * data['totalHospitalBeds']) - impactSevereCasesByRequestedTime)
	impactCasesForICUByRequestedTime = math.trunc(0.05 * impactInfectionsByRequestedTime)
	impactCasesForVentilatorsByRequestedTime = math.trunc(0.02 * impactInfectionsByRequestedTime)
	impactDollarsInFlight = math.trunc(((impactInfectionsByRequestedTime * data["region"]['avgDailyIncomePopulation']) * data["region"]['avgDailyIncomeInUSD']) // timeInDays)

	#Compute estimates:
	##Severe Impact computation
	severeImpactCurrentlyInfected = data['reportedCases'] * 50
	severeImpactInfectionsByRequestedTime = severeImpactCurrentlyInfected * (2 ** (timeInDays // 3))
	severeImpactSevereCasesByRequestedTime =  math.trunc(0.15 * severeImpactInfectionsByRequestedTime)
	severeImpactHospitalBedsByRequestedTime = math.trunc((0.35 * data['totalHospitalBeds']) - severeImpactSevereCasesByRequestedTime)
	severeImpactCasesForICUByRequestedTime = math.trunc(0.05 * severeImpactInfectionsByRequestedTime)
	severeImpactCasesForVentilatorsByRequestedTime = math.trunc(0.02 * severeImpactInfectionsByRequestedTime)
	severeImpactDollarsInFlight = math.trunc(((severeImpactInfectionsByRequestedTime * data["region"]['avgDailyIncomePopulation']) * data["region"]['avgDailyIncomeInUSD']) // timeInDays)

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