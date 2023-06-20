def check_voting_eligibility(age):
    if age < 18:
        print("Not eligible for voting")
    else:
        print("Eligible for voting")


age1 = 16
check_voting_eligibility(age1)

age2 = 21
check_voting_eligibility(age2)