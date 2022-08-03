CREATE TABLE Increment.StockPriceHistoryMinute
(
	Symbol			varchar(10) not null,
	Stockdatetime	datetime2	not null,
	[Open]			float		not null,
	[High]			float		not null,
	[Low]			float		not null,
	[Close]			float		not null,
	[Volume]		float		not null,
	Dividends		float		not null,
	StockSplits		float		not null,
	PRIMARY KEY(Symbol,Stockdatetime)
)
