
show_data = {
    "Chhota Bheem": "brave boy strength Laddu village adventure friends",
    "Doraemon": "robot cat gadgets Doracake Mouse- fear future school boy",
    "Oggy and the Cockroaches": "silent comedy fight Cockroaches funny home",
    "Mr. Bean": "silent man comedy funny clumsy trouble",
    "Horrid Henry": "naughty kid mischief trouble school home",
    "Huddy Mera Buddy": "friendship fun kids robot bond adventure"
}


def count_common_words(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    return len(words1 & words2)

def suggest_similar(input_show):
    if input_show not in show_data:
        print(f"'{input_show}' not found in list.")
        return

    main_keywords = show_data[input_show]
    recommendations = []

    for other_title, other_keywords in show_data.items():
        if other_title == input_show:
            continue
        match_score = count_common_words(main_keywords, other_keywords)
        recommendations.append((other_title, match_score))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    print(f"\nIf you like '{input_show}', you might also enjoy:")
    for title, score in recommendations[:3]:
        print(f"- {title} (match score: {score})")

user_choice = input("Enter a show you enjoy: ")
suggest_similar(user_choice)
