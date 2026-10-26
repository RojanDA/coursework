def probability_no_match(n, days=365):
    prob = 1.0
    for i in range(n):
        prob *= (days - i) / days
    return prob
 
 
print(f"{'No. of people':<15}{'Prob not matching':<20}{'Prob matching':<18}{'Percentage (%)'}")
for people in range(1, 28):
    p_no_match = probability_no_match(people)
    p_match = 1 - p_no_match
    print(f"{people:<15}{p_no_match:<20.10f}{p_match:<18.10f}{p_match * 100:.4f}")
