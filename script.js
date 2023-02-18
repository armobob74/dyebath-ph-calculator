const kb = {
	'na2co3':1.659586e-4, //from wikipedia, where they say pka = 10.22
}
const molar_mass = {
	'na2co3': 105.99, // g/mol, from wikipedia.
}
function calculate_mass(target_ph,water_vol){
	let mass_required = 10 ** (2 * (target_ph - 14)) * molar_mass['na2co3'] * water_vol / kb['na2co3']
	let message = `To get a a <strong>${water_vol}L</strong> solution with a pH of <strong>${target_ph}</strong>, you need <strong>${mass_required.toFixed(1)}g</strong>  of Soda Ash`;
	return {message: message, mass_required:mass_required}
}
function updatePage(){

	let target_ph = document.getElementById('target_ph').value;
	let water_vol = document.getElementById('water_vol').value;

	if(!target_ph)target_ph = 11.00;
	if(!water_vol)water_vol = 3;

	let data = calculate_mass(target_ph,water_vol);
	document.getElementById('display_message').innerHTML = data.message;
	//document.getElementById('display_cost').innerHTML = data.mass_required;
}

