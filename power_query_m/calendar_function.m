/*
================================================================================
  Power Query (M) Dynamic Calendar Function
================================================================================
  Instructions:
  1. In Power BI Desktop: "Transform data" (opens Power Query Editor).
  2. Right-click Queries pane -> New Query -> Blank Query.
  3. Advanced Editor -> paste this script.
  4. Rename query to 'fxCalendar' or invoke it with StartDate and EndDate.
================================================================================
*/

let
    GenerateCalendar = (StartDate as date, EndDate as date) as table =>
    let
        DayCount = Duration.Days(Duration.From(EndDate - StartDate)) + 1,
        Source = List.Dates(StartDate, DayCount, #duration(1, 0, 0, 0)),
        TableFromList = Table.FromList(Source, Splitter.SplitByNothing(), {"Date"}, null, ExtraValues.Error),
        ChangedType = Table.TransformColumnTypes(TableFromList, {{"Date", type date}}),
        AddYear = Table.AddColumn(ChangedType, "Year", each Date.Year([Date]), Int64.Type),
        AddQuarterNumber = Table.AddColumn(AddYear, "Quarter Number", each Date.QuarterOfYear([Date]), Int64.Type),
        AddQuarter = Table.AddColumn(AddQuarterNumber, "Quarter", each "Q" & Text.From([Quarter Number]), type text),
        AddMonthNumber = Table.AddColumn(AddQuarter, "Month Number", each Date.Month([Date]), Int64.Type),
        AddMonthName = Table.AddColumn(AddMonthNumber, "Month Name", each Date.MonthName([Date]), type text),
        AddMonthShort = Table.AddColumn(AddMonthName, "Month Short", each Text.Start([Month Name], 3), type text),
        AddYearMonth = Table.AddColumn(AddMonthShort, "Year Month", each Text.From([Year]) & "-" & Text.PadStart(Text.From([Month Number]), 2, "0"), type text),
        AddDayOfMonth = Table.AddColumn(AddYearMonth, "Day of Month", each Date.Day([Date]), Int64.Type),
        AddDayOfWeek = Table.AddColumn(AddDayOfMonth, "Day of Week Number", each Date.DayOfWeek([Date], Day.Monday) + 1, Int64.Type),
        AddDayOfWeekName = Table.AddColumn(AddDayOfWeek, "Day of Week Name", each Date.DayOfWeekName([Date]), type text),
        AddIsWeekend = Table.AddColumn(AddDayOfWeekName, "Is Weekend", each if [Day of Week Number] >= 6 then "Weekend" else "Weekday", type text)
    in
        AddIsWeekend
in
    GenerateCalendar
