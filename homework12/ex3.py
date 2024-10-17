class LargestProduct:
    def __init__(self, input_list):
        self.input_list = input_list
    def largest_product(self):
        return max(self.input_list[i] * self.input_list[i + 1] for i in range(len(self.input_list) - 1))

input_list = [3,6,-2,-5,7,3] 
largest_product = LargestProduct(input_list)
print(largest_product.largest_product())   