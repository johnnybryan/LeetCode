class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings
        self.size = len(foods)
        # foodToCuisine is a map where key will be the food item and value will be the cuisine
        # cuisineToFood will be a dict of minheaps were food and ratings are stored as a tuple in values with cuisine as key
        # ratingMap contains foods as key and their ratings as values
        self.foodToCuisine, self.ratingMap, self.cuisineToFood = self.initialize()
    
    #Method to initialize our 3 hashMaps
    def initialize(self):
        foodToCuisine, ratingMap = {}, {}
        cuisineToFood = defaultdict(list)
        for i in range(self.size):
            foodToCuisine[self.foods[i]] = self.cuisines[i]
            heapq.heappush(cuisineToFood[self.cuisines[i]], (-self.ratings[i], self.foods[i]))
            ratingMap[self.foods[i]] = self.ratings[i]
        return foodToCuisine, ratingMap, cuisineToFood
        
    # Due to cuisineToFood hashMap, this method becomes an easy O(log(n)) method while changing the rating is constant time because of ratingMap
    def changeRating(self, food: str, newRating: int) -> None:
        self.ratingMap[food] = newRating
        # New rating is pushed in the heap
        heapq.heappush(self.cuisineToFood[self.foodToCuisine[food]], (-newRating, food))  
    
    # RatingMap contains the latest rating of the food whereas the cuisineToFood contains all the ratings.
    def highestRated(self, cuisine: str) -> str:
        rating, food = self.cuisineToFood[cuisine][0]
        #While loop to fetch the exact latest rating from all the ratings we have
        while -rating != self.ratingMap[food]:
            heapq.heappop(self.cuisineToFood[cuisine])
            rating,food = self.cuisineToFood[cuisine][0]
        return food
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)