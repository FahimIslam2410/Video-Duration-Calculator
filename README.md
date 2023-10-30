# Video-Duration-Calculator
---

## Overview

The **Video Duration Calculator** is a simple Python program that allows users to input video durations in the format of minutes and seconds (mm:ss). The program accumulates the input durations and, when the user presses 'q', calculates and displays the total duration in the format of hours:minutes:seconds.

## Usage

1. Run the program by executing the script in a Python environment.

   ```bash
   python video_duration_calculator.py
   ```

2. The program will start, and you will see the following:


   ```
   ######### Video Duration Calculator #########
         Press 'q' to get the final total.
   ```

3. Enter video durations in the format mm:ss (e.g., 24:10) and press Enter. The program will add the input duration to the total and display the current total.

4. To get the final total, press 'q'. The program will calculate and display the final video duration total in the format hh:mm:ss.

5. If you input an invalid format, the program will display an error message: "Invalid input. Please use the mm:ss format."

6. You can continue entering video durations or press 'q' to get the final total whenever you like.

## Sample Usage

Here's an example of how to use the Video Duration Calculator:

```
######### Video Duration Calculator #########
      Press 'q' to get the final total.

Enter video duration (mm:ss): 15:30
Current total: 00:15:30

Enter video duration (mm:ss): 10:45
Current total: 00:26:15

Enter video duration (mm:ss): 5:20
Current total: 00:31:35

Enter video duration (mm:ss): q
Generating total time...
Final video duration total: 00:31:35
```

