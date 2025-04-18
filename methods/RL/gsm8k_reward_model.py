"""
GSM8KRewardModel - Helper class for evaluating and scoring GSM8K equations
"""


import re
import operator




class GSM8KRewardModel:
   def __init__(self, answer):
       """
       Initialize the GSM8KRewardModel with a solution number


       Args:
           answer (float): The solution to the problem
       """
       self.answer = answer




   def compute_score(self, solution_str, format_score=0.1, success_score=1.0, debug=False):
       """
       Compute a score for the given solution.


       Args:
           solution_str (str): The full solution string
           format_score (float): Score for correct format but wrong answer
           success_score (float): Score for correct answer
           debug (bool): Whether to print debug information


       Returns:
           float: Score between 0.0 and success_score
       """
       valid, output_solution = self.extract_solution(solution_str)


       if not valid:
           return format_score
      
       if debug:
           print(f"--------------------------------")
           print(f"Answer: {self.answer} | Output: {output_solution}")
           print(f"Solution string: {solution_str}")


       if abs(self.answer - output_solution) < 1e-5:
           return success_score
      
       return format_score


   def extract_solution(self, answer_str):
       """
       Extract the solution from the GSM8K answer.


       Args:
           answer_str (string): Given answer for GSM8K problem including reasoning


       Returns:
           tuple: (bool, float) - Success status and solution number
       """


       # Look for the explicit marker in the format '#### NUMBER'
       import re
      
       # Look for content between <answer> and </answer> tags
       answer_match = re.search(r'<answer>\s*(.*?)\s*</answer>', answer_str, re.DOTALL)
      
       if answer_match:
           try:
               # Extract the content from the tags
               answer_content = answer_match.group(1)


               # Now find floats within that content
               float_match = re.search(r'-?\d+(?:\.\d+)?', answer_content)
               if float_match:
                   solution = float(float_match.group(0))
                   return True, solution
           except (ValueError, AttributeError):
               pass
      
       return False, ""


if __name__ == "__main__":
   # Example usage
   model = GSM8KRewardModel(25)


   # Test scoring
   print("\nScoring solutions:")
   solution1 = "Let me solve this step by step.\n<think>Example prompt of gsm8k thinking.</think>\n\n<answer>25</answer>"


   print(model.compute_score(solution1, debug=True))

