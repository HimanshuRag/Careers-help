import argparse
from evaluation import evaluate_job_description
from resume import plan_resume_updates
from cover_letter import plan_cover_letter


def main():
    """Command-line interface for job evaluation and resume/cover letter planning."""
    parser = argparse.ArgumentParser(
        description="Evaluate a job description and get resume/cover letter suggestions."
    )
    parser.add_argument(
        "description_file",
        help="Path to a text file containing the job description to evaluate.",
    )
    args = parser.parse_args()

    # Read the job description from the provided file
    with open(args.description_file, "r", encoding="utf-8") as f:
        description = f.read()

    # Evaluate the job description across dimensions
    result = evaluate_job_description(description)

    # Print the raw evaluation result
    print("Evaluation result:")
    for dim, score in result.scores.items():
        print(f"  {dim}: {score}")
    print(f"Overall score: {result.score}")
    print(f"Grade: {result.grade}")

    # Generate suggestions for updating your resume
    resume_plan = plan_resume_updates(result)
    print("\nResume suggestions:")
    for dim, suggestion in resume_plan.items():
        print(f"  {dim}: {suggestion}")

    # Generate a plan for your cover letter
    cover_letter_plan = plan_cover_letter(result)
    print("\nCover letter suggestions:")
    for section, suggestion in cover_letter_plan.items():
        print(f"  {section}: {suggestion}")


if __name__ == "__main__":
    main()
