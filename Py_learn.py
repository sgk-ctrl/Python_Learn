def main() -> None:
	tweet = input("Enter your tweet: ")
	max_length = 140
	tweet_length = len(tweet)

	if tweet_length > max_length:
		extra_characters = tweet_length - max_length
		print(
			f"Your message is {extra_characters} characters longer than the allowable {max_length} character limit."
		)
	else:
		remaining_characters = max_length - tweet_length
		print(
			f"Your message is within the limit. You have {remaining_characters} characters remaining."
		)


if __name__ == "__main__":
	main()
