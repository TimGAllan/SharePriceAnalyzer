CREATE TABLE Fact.StockPriceHistoryMinute
(
	Symbol			varchar(10) not null,
	StockDatetime	datetime2	not null,
	StockDate		date		not null,
	Stocktime		time		not null,
	[Open]			float		not null,
	[High]			float		not null,
	[Low]			float		not null,
	[Close]			float		not null,
	[Volume]		float		not null,
	Dividends		float		not null,
	StockSplits		float		not null,
	PRIMARY KEY(Symbol,Stocktime)
)