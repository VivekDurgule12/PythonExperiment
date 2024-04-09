class EligibleforEntrance(Exception):
    pass

class NotEligibleforEntrance(Exception):
    pass

def check_eligibility(p_marks):
    if p_marks < 45:
        raise NotEligibleforEntrance("You are not eligible for entrance.")
    else:
        raise EligibleforEntrance("You are eligible for entrance.")

try:
    pcm_marks = float(input("Enter PCM marks: "))
    check_eligibility(pcm_marks)
except ValueError:
    print("Invalid input! Please enter a valid number.")
except NotEligibleforEntrance as e:
    print(e)
except EligibleforEntrance as e:
    print(e)
