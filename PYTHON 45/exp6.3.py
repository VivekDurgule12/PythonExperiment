class EligibleforEntrance(Exception):
    pass

class NotEligibleforEntrance(Exception):
    pass

try:
    pcm_marks = int(input("Enter your PCM marks: "))
    if pcm_marks < 45:
        raise NotEligibleforEntrance("Your PCM marks are not sufficient for entrance.")
    else:
        raise EligibleforEntrance("Congratulations! You are eligible for entrance.")
except NotEligibleforEntrance as e:
    print(e)
except EligibleforEntrance as e:
    print(e)
