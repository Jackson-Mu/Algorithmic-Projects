#===============================================================================================================================
# Name         : Question Answering
# Author       : Jackson Mukeshimana
# Version      : 01
# Date Created : 24/04/2024
# Date Modified: 24/04/2024
# Description  : Greedy Algorithm Implementation for the Questions Answering with Associated Probability
#================================================================================================================================



def maximize_expected_total_value(questions):
    num_questions = len(questions)
    
    # Step 1: Sort questions by expected value
    questions.sort(key=lambda x: x[1] * x[2], reverse=True)
    
    # Initialize variables
    expected_total_value = 0
    prev_correct_prob = 1  # Previous cumulative correct probability
    cumulative_delay = 0   # Cumulative delay
    
    # Step 2: Iterate through sorted questions
    for i in range(num_questions):
        question = questions[i]
        p_i = question[2]  # Probability of answering correctly
        d_i = question[1]  # Delay for the question
        
        # Calculate the expected value for the current question and update cumulative values
        expected_total_value += prev_correct_prob * (1 - p_i) * cumulative_delay
        prev_correct_prob *= p_i
        cumulative_delay += d_i
    
    # Add the final term to the expected total value
    expected_total_value += prev_correct_prob * cumulative_delay
    
    return expected_total_value

# Example usage
arr = [['Q1', 1, 0.9], ['Q2', 1, 0.8], ['Q3', 2, 0.5], ['Q4', 2, 0.3], ['Q5', 3, 0.5], ['Q6', 4, 0.2]]
max_expected_value = maximize_expected_total_value(arr)
print("Maximum expected total value:", max_expected_value)



