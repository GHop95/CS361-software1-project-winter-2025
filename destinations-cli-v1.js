const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function askQuestion(query) {
    return new Promise(resolve => {
        rl.question(query, answer => {
            resolve(answer);
        });
    });
}

let locationsArray = [];

function Location(city_in, state_in, notes_in) {
	this.city = city_in;
	this.state = state_in;
	this.notes = notes_in;
}

function view_list() {
	if (locationsArray.length === 0) {
        console.log("The current list is empty.\n");
        return;
    }

	console.log("Currently viewing saved locations:\n");
	for (let i= 0; i < locationsArray.length; i++) {
	console.log(
`${i+1}. ${locationsArray[i].city}, ${locationsArray[i].state}
   note:  ${locationsArray[i].notes}`);
	}
	console.log("")
}

async function add_to_list() {

	let confirmAdd = await askQuestion(
`Do you wish to add a location to your list?
1. Yes    0. No\n`)
	if (confirmAdd == 0) {
		return;
	} else if (confirmAdd != 1) {
		console.log("Unexpected input received. Cancelling add...\n")
		return;
	}

	console.log("")
	let city = await askQuestion("Enter the city: \n   ");
	let state = await askQuestion("Enter the state/province: \n   ");
	let notes = await askQuestion("Enter any additional notes: \n   ");

	let newLocation = new Location(city, state, notes); 
	locationsArray.push(newLocation);
	console.log("* Location added successfully!\n");
	return;
}

async function delete_from_list() {
	if (locationsArray.length === 0) {
        console.log("* The current list is empty.\n");
        return;
    }
	view_list();
	let delete_me = await askQuestion("Enter the number of the location you want to delete: \n");
	delete_me = parseInt(delete_me)

	if (isNaN(delete_me) || delete_me < 1 || delete_me > locationsArray.length) {
        console.log("* Invalid selection.\n");
        return;
    }

	let confirmDelete = await askQuestion(
`You are about to delete ${locationsArray[delete_me-1].city}, ${locationsArray[delete_me-1].state}. 
Do you wish to continue?
    1. Yes    0. No\n`)
	if (confirmDelete == 0) {
		return;
	} else if (confirmDelete != 1) {
		console.log("Unexpected input received. Cancelling delete...\n")
		return;
	}

	locationsArray.splice(delete_me-1, 1) //arg1 = index to delete, arg2 = how many elements to delete.
	console.log("\n* Location removed successfully!\n");
}

function print_help() {
	console.log(
`HELP Information:
In this app, you can create your own list of locations that you would like to visit.
Currently you can add a location to your list manually by entering in the values of each location.
Soon there will be other methods to add locations to your list.
When you are at the main menu, press 2 and then ENTER to enter add mode.
You will be asked if you want to continue. Press 1 if you still want to add a location.
You will then be prompted to enter a value for each of the necessary fields.

It's easy to delete locations on the fly, so we encourage you to experiment.
You will be asked if you are certain when you attempt to delete an item from your list.\n`)
}

function print_credits() {
	console.log(
`CREDITS
Designer, Programmer: Grant Hopkin \n`)
}

function print_menu() {
	console.log(`What would you like to do? 
   1. View your locations list
   2. Add location to list
   3. Delete location from list
   4. Help
   5. Credits
   0. Quit program `)
}

async function main() {
	//print intro
	console.log("\nDestination Tracker V1.0\n");
	//print instructions
	console.log(
`Welcome to Destination Tracker! In this app, you can create a list of travel destinations you wish visit.
You will have several options from the main menu, such as viewing your current list, 
adding to your list, deleting from your list, or reading a help tab in case you get stuck. \n`)
	//ask confirmation
	await askQuestion("Press ENTER to continue:\n");
    let choice = -1;

	do {
		print_menu()
		choice = await askQuestion("");
		console.log("");
		if (choice == 1) {
			//view list
			view_list()
			await askQuestion("Press ENTER to continue:\n");
		} else if (choice == 2) {
			// add list
			await add_to_list()
			// need await to ensure that main() waits for user input.
		} else if (choice == 3) {
			// delete
			await delete_from_list()
		} else if (choice == 4) {
			// help
			print_help()
		} else if (choice == 5) {
			// credits
			print_credits()
		} else if (choice == 0) {
			console.log("You chose quit program.")
		} else {
			console.log("Invalid input, please enter a valid number.")
		}
	} while (choice != 0);
	console.log("Goodbye!\n")

	rl.close();
}

main();