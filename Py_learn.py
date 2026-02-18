def get_bmi_category(bmi: float) -> str:
	if bmi < 18.5:
		return "underweight"
	if bmi < 25:
		return "normal"
	if bmi < 30:
		return "overweight"
	if bmi < 35:
		return "moderately obese"
	if bmi < 40:
		return "overly obese"
	return "morbidly obese"


def main() -> None:
	height_cm = float(input("Enter height in cm: "))
	weight_kg = float(input("Enter weight in kg: "))

	if height_cm <= 0 or weight_kg <= 0:
		print("Height and weight must be positive numbers.")
		return

	height_m = height_cm / 100
	bmi = weight_kg / (height_m * height_m)
	category = get_bmi_category(bmi)

	print(f"BMI: {bmi:.2f}")
	print(f"Category: {category}")


if __name__ == "__main__":
	main()
