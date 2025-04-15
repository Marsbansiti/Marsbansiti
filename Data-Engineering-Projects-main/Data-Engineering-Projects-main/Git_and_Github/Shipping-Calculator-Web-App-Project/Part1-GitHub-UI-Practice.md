
# 🚀 Practice Project: Part 1 - GitHub UI

---

## 📘 Overview

you will start your journey with the GitHub implementation for your organization by creating a repository in your GitHub account and initializing it with a `README.md` file and a License.

You will then:
- Update the `README.md` file
- Add a **Code of Conduct**
- Create **Contribution Guidelines**
- Create a new branch
- Add code for Shipping logistics calculation
- Merge changes to the `main` branch using a Pull Request

---

## 🎯 Objectives

By the end of this lab, you will be able to:

✅ Create a repository with a `README.md` file and a license  
✅ Update existing files  
✅ Commit changes to your repository  
✅ Create a new branch and add files to it  
✅ Merge the branch to the main using a Pull Request

---

## 🧩 Task 1: Create a Repository with README and License

1. Click the **+** icon at the top right of GitHub and select **New repository**
2. Name the repository `LogisticsShippingRates`
3. Make sure it is **Public**
4. Select **Add a README file**
5. Choose **Apache License 2.0**
6. Click **Create repository**

✅ You should now see the new repo containing `README.md` and `LICENSE`.

---

## 📝 Task 2: Update the README File

1. Click on `README.md`, then click the **pencil icon** to edit.
2. Add the following section:

```markdown
## Please consider the below factors while contributing

**Code Style:**  
Maintain a consistent code style for readability.

**Documentation:**  
Ensure well-documented code for effective collaboration.

**Testing:**  
Thoroughly test your changes before submitting a pull request.

**Issue Tracker:**  
Check the Issue Tracker for tasks.

**Code Review:**  
All contributions undergo a code review process.

**Licensing:**  
Contributions are licensed.
```

3. Add a commit message and select "Commit directly to the main branch"
4. Click **Commit changes**

> ✅ Tip: If you don’t see the Commit radio button, zoom out or scroll down.

---

## 🤝 Task 3: Add a Code of Conduct

1. Click **Add file > Create new file**
2. Name the file `CODE_OF_CONDUCT.md`
3. Click on **Choose a code of conduct template**
4. Select **Contributor Covenant** (Recommended for projects of all sizes)

Your `CODE_OF_CONDUCT.md` will include the following:
```markdown
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our community a harassment-free experience for everyone, regardless of age, body size, visible or invisible disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming, diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our community include:

- Demonstrating empathy and kindness toward other people
- Being respectful of differing opinions, viewpoints, and experiences
```

5. Fill in the **Contact method** field if required
6. Click **Review and submit**
7. Scroll and click **Commit changes** directly to the `main` branch


✅ You have successfully added a Code of Conduct.
---

## 🛠️ Task 4: Add Contribution Guidelines

1. Click **Add file > Create new file**
2. Name the file `CONTRIBUTING.md`
3. Add the following content:

```markdown
# Contribution Guidelines

**Welcome Contributors!**

Thank you for considering contributing to the centralized repository. This document outlines the guidelines for contributing to the development of Shipping Rates and Calculations.

## Code Style
Please follow the coding style and conventions used in the existing codebase. This helps maintain consistency across the project.

## Documentation
Ensure that your contributions are well-documented. Include comments in your code where necessary and provide a clear and concise description of your changes in the pull request.

## Testing
Before submitting a pull request, make sure your changes have been tested thoroughly. Include relevant test cases and ensure that existing tests pass.

## Issue Tracker
Check the issue tracker for any open issues or feature requests. If you're working on something, please comment on the issue to let others know.

## Code Review
All contributions will go through a code review process. Be open to feedback and be willing to make changes if necessary. Code reviews help maintain code quality and consistency.

**Thank you for your contribution!**
```

4. Click **Commit changes** directly to the `main` branch

✅ You have now added contribution guidelines to your project.

---

## 🌿 Task 5: Create a New Branch

1. Click on the **Branch dropdown**
2. Click **New Branch**
3. Name it: `Shipping_Calculation`
4. Click **Create Branch**

---

## 📄 Task 6: Add Shipping Calculator Code

1. Switch to the `Shipping_Calculation` branch
2. Create a new file: `Shipping_Cost_Calculator.py`
3. Add the following code:

```python
# Shipping Cost Calculator

# Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

# Calculate shipping cost
shipping_cost = weight * rate

# Display the result
print(f"Shipping Cost: {shipping_cost} USD")
```

4. Commit the file directly to the `Shipping_Calculation` branch

✅ Your feature branch now contains the shipping calculator code.

---

## 🔀 Task 7: Create a Pull Request

1. Go to the **Pull Requests** tab
2. Click on **Compare & pull request**
3. Add a commit message
4. Click **Create pull request**

---

## ✅ Task 8: Merge the Branch to Main

1. Click **Merge pull request**
2. Click **Confirm merge**

🎉 You should now see `Shipping_Cost_Calculator.py` in your `main` branch.

---

## 🎉 Congratulations!

 you have:

- Created a GitHub repository with a README and License
- Edited the README file
- Added a Code of Conduct
- Added Contribution Guidelines
- Created a new branch and added a Python shipping calculator
- Merged your changes using a Pull Request

You’ve successfully demonstrated core GitHub collaboration skills using the GitHub UI! 🚀
