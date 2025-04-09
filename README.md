# TPS25 - W1D5 - Python APIs: Dog Image Browser

## Assignment Overview

You will build a Python script that interacts with the Dog CEO REST API to create a Dog Image Browser. The application allows users to view a list of all available dog breeds, get random images of specific breeds, and get random images of specific sub-breeds. You'll use the `requests` library to make HTTP requests and handle API responses.

## Learning Objectives

- Use the `requests` library to make HTTP GET requests to a REST API
- Parse JSON responses from API calls
- Handle API errors and connection issues with `try/except` blocks
- Work with nested data structures (dictionaries and lists)
- Write clean, modular, and testable code
- Run and understand test results using `unittest`

## Getting Started with GitHub Classroom and Codespaces

### Accepting the Assignment

1. Click on the GitHub Classroom assignment link provided by your instructor
2. Authorize GitHub Classroom if prompted
3. Accept the assignment
4. Wait for your repository to be created

### Opening the Assignment in Codespaces

1. Once your repository is ready, click on the "Code" button
2. Select the "Codespaces" tab
3. Click "Create codespace on main"
4. Wait for your Codespace to be set up — this may take a few minutes

## Instructions

1. In your Codespace, you'll find the following files:

   - `dog_api.py` (starter file with comments to guide your implementation)
   - `dog_api_tests.py` (test suite to validate your logic — do not modify)
   - `.github` folder (for GitHub Classroom Autograding — do not modify)
   - `README.md` (this file with instructions)
   - `.gitignore` (standard Python gitignore file)

2. Complete the following in `dog_api.py`:

   - Implement the `get_random_image()` function:

     - Make a request to `https://dog.ceo/api/breed/{breed}/images/random`
     - Return the image URL or handle errors appropriately

   - Implement the `get_random_sub_breed_image()` function:

     - Make a request to `https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random`
     - Return the image URL or handle errors appropriately

   - Implement the `show_breeds()` function:

     - Print all breeds (sorted), 5 per line

   - Complete the main function logic:
     - Check if a breed exists before fetching an image
     - Check if a breed has sub-breeds before asking for a sub-breed
     - Check if a sub-breed is valid before fetching an image
     - Print image URLs or error messages

3. Run the tests to verify your implementation:

   ```
   python -m unittest dog_api_tests.py -v
   ```

4. Test your program manually by running:
   ```
   python dog_api.py
   ```

## Example Output

When your program is working correctly, it should behave like this:

```
What would you like to do?
1. Show all breeds
2. Get a random image from a breed
3. Get a random image from a sub-breed
4. Exit

Enter your choice (1-4): 1
affenpinscher, african, airedale, akita, american
bulldog, american, australian, basset, beagle
...

What would you like to do?
1. Show all breeds
2. Get a random image from a breed
3. Get a random image from a sub-breed
4. Exit

Enter your choice (1-4): 2
Enter breed name: husky
Random image URL for husky: https://images.dog.ceo/breeds/husky/n02110185_10047.jpg

What would you like to do?
1. Show all breeds
2. Get a random image from a breed
3. Get a random image from a sub-breed
4. Exit

Enter your choice (1-4): 3
Enter breed name: bulldog
Available sub-breeds for bulldog:
1. boston
2. english
3. french
Enter sub-breed name: english
Random image URL for bulldog (english): https://images.dog.ceo/breeds/bulldog-english/n02096585_345.jpg
```

## Error Handling

Your application should handle the following errors:

- Invalid menu options
- Non-existent breeds
- Breeds without sub-breeds
- Non-existent sub-breeds
- API connection errors

For each error, display a user-friendly message and allow the user to try again.

## Submission Guidelines

1. Complete the implementation in your GitHub Codespace
2. Make sure all your changes are committed and pushed to your repository
3. Run the `python -m unittest dog_api_tests.py -v` command to execute the test cases and verify that all tests pass
4. Take a screenshot of the passing tests
5. Submit both your GitHub repository link and the screenshot through Canvas
