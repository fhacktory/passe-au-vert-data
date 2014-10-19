/* Model */
/*
var trafficLight = {
    offset: 0, // Time to first Red to Green change (in milliseconds)
    cycle_time: 10000, // (in milliseconds)
    green_cycle_time: 4000, // (in milliseconds)
    orange_cycle_time: 1000, // (in milliseconds)
    red_cycle_time: 3000, // (in milliseconds)
};
*/

function trafficLightState(trafficLight, time) {
	var state = {}, cycleOffset;

	cycleOffset = time % trafficLight.cycle_time;
	cycleOffset -= trafficLight.offset;
	if (cycleOffset < 0) {
		cycleOffset += trafficLight.cycle_time;
	}

	if (cycleOffset < trafficLight.green_cycle_time) {
		state.state = "Green";
		state.remaining_time = trafficLight.green_cycle_time - cycleOffset;
	} else if (cycleOffset < trafficLight.green_cycle_time + trafficLight.orange_cycle_time) {
		state.state = "Orange";
		state.remaining_time = (trafficLight.green_cycle_time + trafficLight.orange_cycle_time) - cycleOffset;
	} else {
		state.state = "Red";
		state.remaining_time = trafficLight.cycle_time - cycleOffset;
	}

	return state;
}

/* Tests */
/*
console.log(trafficLightState(trafficLight, 300));
console.log(trafficLightState(trafficLight, 4020));
console.log(trafficLightState(trafficLight, 5090));

console.log(trafficLightState(trafficLight, 204020));
*/
