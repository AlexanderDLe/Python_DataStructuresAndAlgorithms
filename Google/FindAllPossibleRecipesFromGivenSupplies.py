'''

  2115. Find All Possible Recipes from Given Supplies

'''

from collections import Counter, defaultdict


class Solution:
  def findAllRecipes(self, recipes, ingredients, supplies):
    self.n = len(recipes)
    self.recipeSet = set(recipes)
    suppliesSet = set(supplies)
    
    recipeToIndex = {x:i for i, x in enumerate(recipes)}
    dependencies, inDegrees, queue = self.init(recipes, ingredients)
    result = []
    
    while queue:
      for _ in range(len(queue)):
        item = queue.pop(0)
        index = recipeToIndex[item]
        canBeMade = True
        
        for ingredient in ingredients[index]:
          if ingredient not in suppliesSet: 
            canBeMade = False
            break        
        
        if canBeMade == False: continue
        
        suppliesSet.add(item)
        result.append(item)
        if item not in dependencies: continue
        
        for child in dependencies[item]:
          inDegrees[child] -= 1
          if inDegrees[child] == 0: queue.append(child)
        
    
    return result
    
  def init(self, recipes, ingredients):
    parentToChild = defaultdict(list)
    inDegrees = defaultdict(int)
    sources = set(recipes)
    
    for recipe, ingredientsForRecipe in zip(recipes, ingredients):
      for ingredient in ingredientsForRecipe:
        if ingredient in self.recipeSet:
          parentToChild[ingredient].append(recipe)
          inDegrees[recipe] += 1
          if recipe in sources: sources.remove(recipe)
    
    return (parentToChild, inDegrees, list(sources))
  
  
class Solution2:
  def findAllRecipes(self, recipes, ingredients, supplies):
    ingredientToRecipe, inDegree = defaultdict(set), Counter()
    
    # Construct directed graph and count the in-degrees
    for recipe, ingredient in zip(recipes, ingredients):
      for ing in ingredient:
        ingredientToRecipe[ing].add(recipe)
      inDegree[recipe] = len(ingredient)
      
    # Topological Sort
    ans = []
    for ing in supplies:
      for recipe in ingredientToRecipe.pop(ing, set()):
        inDegree[recipe] -= 1
        if inDegree[recipe] == 0:
          supplies.append(recipe)
          ans.append(recipe)
    
    return ans
    
  
def runSolution():
  solution = Solution2()
  print(solution.findAllRecipes(
    recipes     = ["bread"], 
    ingredients = [["yeast","flour"]], 
    supplies    = ["yeast","flour","corn"]
  ))
  print(solution.findAllRecipes(
    recipes     = ["bread","sandwich"], 
    ingredients = [["yeast","flour"],["bread","meat"]], 
    supplies    = ["yeast","flour","meat"]
  ))
  print(solution.findAllRecipes(
    recipes     = ["bread","sandwich","burger"], 
    ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], 
    supplies    = ["yeast","flour","meat"]
  ))
  pass
runSolution()