# Assignment #2

## 1. Reflections

  ### 1.1 Computer Mouse
  - Check left and right button functionality.
  - Test the scroll wheel for smooth scrolling.
  - Verify the accuracy and responsiveness of the mouse sensor.
  - Verify that the mouse design accommodates different hand sizes and grip styles.
  - Test the mouse's tracking accuracy on various surfaces, including mouse pads and different desk materials.
  - Measure the mouse's battery life under typical usage conditions.
      
  ### 1.2 Catastrophic Failure
  
  The Therac-25 was a medical linear accelerator used for radiation therapy in the treatment of cancer. It was manufactured by Atomic Energy of Canada Limited (AECL) in the 1980s. The machine had two software-related accidents that resulted in fatal overdoses to patients:

June 1985 Incident: In this case, a software defect caused the machine to deliver a 100 times higher radiation dose to a patient named Lea Dickson than intended. She suffered severe radiation burns and died as a result.

January 1987 Incident: A similar accident occurred, but this time, the machine delivered an even higher dose to another patient, resulting in severe injuries.

The Therac-25 incidents were primarily caused by race conditions in the software. A race condition occurs when two or more processes compete for shared resources and the final outcome depends on the timing of the processes. In the Therac-25's case, the race condition led to incorrect high doses of radiation.

To prevent these accidents, various tests should have been performed, including:

**Intergration test** : integration testing should have been carried out to identify potential software conflicts and race conditions in the system. The integration of software components and hardware systems should have been thoroughly validated.

**Boundary Testing** : This type of testing focuses on the limits of the system's behavior. It should have included testing the maximum and minimum values for radiation dosage to ensure the system never exceeded safe limits.

**Human Factors Testing** : User interfaces and controls should have been evaluated to ensure that they were intuitive and not prone to user error. Clear and informative error messages should have been provided to alert operators to any issues.
  

## 2. Two Katas

  ### 2.1 String Utility


  ### 2.2 Bowling Game Kata

 


## 3. Investigation of Tools

  ### 3.1 JUnit 5

  #### @Tag
  Labels tests with categories (tags) for better organization.
  #### @Disabled
  Temporarily skips a test without removing it from the code.
  #### @RepeatedTest
  Runs a test multiple times for statistical analysis or to catch intermittent issues.
  #### @BeforeEach, @AfterEach
  Sets up and cleans up before and after each test method.
  #### @BeforeAll, @AfterAll
  Runs once before and after all test methods in a class for one-time setup and cleanup.
  #### @DisplayName
  Gives custom names or descriptions to test methods for better readability and reporting.
  #### @Nested
  Organizes related test methods in nested classes for better structure.
  #### @assumeFalse, @assumeTrue
  Conditionally skips tests based on specific assumptions to handle different scenarios.

  ### 3.2 Mocking Frameworks

  Mockito vs EasyMock

  #### Similarities:
  Both EasyMock and Mockito are Java mocking frameworks that support creating mock objects, verifying interactions, and have relatively simple syntax for unit testing.
  
  #### Differences:
  EasyMock requires a "replay/verify" approach, offering more control but a steeper learning curve. Mockito's "verify" method simplifies verification and tends to result in more readable and concise code.

  #### Preference:
  I personally prefer Mockito for its simplicity and readability. Mockito's straightforward syntax and "verify" method make it easier to work with, resulting in cleaner and more concise test code. While EasyMock     
  offers more control, it has a steeper learning curve and tends to be more verbose in comparison. The choice between the two depends on project requirements and developer familiarity. Both frameworks are effective 
  for unit testing in Java.
