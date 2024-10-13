def learn_from_feedback(user_input, response, feedback, memory):
    if user_input not in memory:
        memory[user_input] = {}

    if response not in memory[user_input]:
        memory[user_input][response] = 0

    if feedback.lower() == "yes":
        memory[user_input][response] += 1
    else:
        memory[user_input][response] -= 1


def choose_best_response(user_input, memory):
    if user_input in memory:
        # Return the best response based on feedback scores
        best_response = max(memory[user_input], key=memory[user_input].get)
        return best_response
    return None
