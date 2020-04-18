Christina Aiello, 2020, Protected under MIT License

Boyfriend needed to reformat some giant CSV files he had, and he was doing it by hand.
He had data with one timestamp column with numerous timestamps in it, columns that represented different data point types, and values in each column representing the value for that data point at that timestamp. What he needed was one row per tuple of (timestamp, data point type, data point value).

 I wrote this for him, and the excessive comments are to teach him how it works, so he can modify the script in the future.

![Screenshot of example input](https://raw.githubusercontent.com/cjaiello/ReformatCsv/master/example-input.png)

![Screenshot of example output](https://raw.githubusercontent.com/cjaiello/ReformatCsv/master/example-output.png)