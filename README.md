# Eco-Solver

This repository contains a Jupyter Notebook designed to solve a game of balancing an ecosystem that is described in detail on various websites online and is entirely based on these descriptions that are publicly available. The game involves creating a valid food chain from a given list of species. Each species has specific attributes such as calories provided, calories needed, and lists of species it can eat and be eaten by. The goal is to determine valid food chains and rank them based on the total calories provided.

## Running the Notebook

You can run the notebook online using Binder. Click the badge below to launch the notebook:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tobias-fritz/eco-solver/HEAD)

## Usage

You can use the notebook in two ways:

### 1. Check if your food chain is valid
- Create a list of `Species` objects.
- Call the `is_valid_food_chain` function.
- If the food chain is valid, the function will return `True` and the number of excess calories.

### 2. Propose all possible food chains, ranked by excess calories
- Add species to the list (the total number of species can be larger than the food chain size).
- Select the number of species you want in the food chain.
- Get the valid food chains with the selected number of species and print the first 5 valid food chains, sorted by the excess calories provided.

## License

This project is licensed under the MIT License.