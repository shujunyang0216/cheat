def cheat(assignment_number: str):
    """This function return solution to some questions on Python programming assignment"""
    if assignment_number == "Q1.2P.1":
        solution = "#!pip install numpy\nimport numpy as np #import numpy"
    elif assignment_number == "Q1.2P.2":
        solution = "another_array = np.zeros((2, 4, 6))\nanother_array[-1, 0, 2]"
    elif assignment_number == "Q1.2P.5":
        solution = ("#change the working directory: cd\n"
                    "#print the current working directory: pwd\n"
                    "#list the contents of the working directory: ls\n"
                    "#list current workspace variables: whos\n")
    elif assignment_number == "Q2.2P.2":
        solution = ("np.random.seed(14506920)\n"
                    "numeric_vec = np.random.uniform(low=0, high=100, size=4)\n"
                    "weight_sum = 0 * 2\n"
                    "for i in range(len(numeric_vec)):\n"
                    "    weight_sum += np.where(i % 2 == 0, numeric_vec[i], numeric_vec[i] * 2)\n"
                    "weight_avg = weight_sum / (np.size(numeric_vec)*1.5)\n")
    else:
        raise Exception("Work by yourself")
    return print(solution)
