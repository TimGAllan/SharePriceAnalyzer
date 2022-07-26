CREATE PROCEDURE Dimension.PopCalendar
AS
BEGIN

	declare @stockDate date = cast('20100101' as date)

	WHILE @stockDate<=CAST('20291231' as date)
	BEGIN

		INSERT Dimension.Calendar
		SELECT @stockDate, year(@stockDate), month(@stockDate)-1/3+1,month(@stockDate)

		set @stockDate = dateadd(dd,1,@stockDate)

	END

END