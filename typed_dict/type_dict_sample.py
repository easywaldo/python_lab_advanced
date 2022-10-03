from typing import TypedDict

class Range(TypedDict):
    min: float
    max: float
    
class NutritionInformation(TypedDict):
    value: int
    unit: str
    confidenceRange95Percent: Range
    standardDeviation: float
    
class RecipeNutritionInformation(TypedDict):
    recipes_used: int
    calories: NutritionInformation
    fat: NutritionInformation
    protein: NutritionInformation
    carbs: NutritionInformation
    
def get_nutrition_from_spoonacular(recipes_name: str):
    result = None
    if "pizza":
        result = RecipeNutritionInformation(
            recipes_used= 12, 
            calories= NutritionInformation(
                value=380, 
                unit="flown",
                confidenceRange95Percent= Range(min=3.0, max=8.0),
                standardDeviation=3.0)
            ,
            fat=NutritionInformation(
                value=200,
                unit="fat_unit",
                confidenceRange95Percent=Range(min=2.0,max=10.0),
                standardDeviation=4.1
            ),
            protein=NutritionInformation(
                value=300,
                unit="good_unit",
                confidenceRange95Percent=Range(min=4.5,max=70.0),
                standardDeviation=3.1
            ),
            carbs=NutritionInformation(
                value=15,
                unit="normal",
                confidenceRange95Percent=Range(min=1.0,max=10.0),
                standardDeviation=2.7
            )
        )
    return result


if __name__ == '__main__':
    nutrition_information: RecipeNutritionInformation = get_nutrition_from_spoonacular("pizza")
    print(nutrition_information)