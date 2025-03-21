#2115 Find All Possible Recipes from Given Supplies
# Date: 21/03/2025
#Type: Daily Problem
# Method used: Graph-Based Approach

from typing import List
class Solution: 
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        all_recipes = [] 
        while True:
            new_recipe_added = False
    
            for i in range(len(ingredients)):
                have_all_ing = True
                
                for j in ingredients[i]:
                    if j not in supplies:
                        have_all_ing = False
                        break
                    
                if have_all_ing:
                    all_recipes.append(recipes[i])
                    supplies.append(recipes[i])  # Add newly created recipe to supplies
                    
                    # Remove the recipe and its ingredients (since it's now created)
                    ingredients.pop(i)
                    recipes.pop(i)
                    
                    new_recipe_added = True
                    break  # Restart the loop since the list has been modified
            
            if not new_recipe_added:
                break  # Exit when no more new recipes can be created
        
        return all_recipes
 
                 
        
        


        