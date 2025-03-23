class dfedit:
    def __init__(self, data):
        self.__ccount = data.shape[1]
        self.__cnames = data.columns
        self.__crows = data.shape[0]
        self.__data = data

    def info(self):
        """General information about the dataframe"""
        print(f"Total columns: {self.__ccount}\nTotal rows: {self.__crows}\n{list(self.__cnames)}")
    def drop_columns(self, columns):
        """Drops the listed columns in the data"""
        self.__data.drop(columns = columns, axis = 1, inplace = True)
        return self.__data
    def uniques(self, name):
        """Returns the unique values of a data column"""
        return self.__data[str(name)].unique()
    def count_na(self):
        columns = list(self.__data.columns)
        for i in columns:
            x = 0
            x = sum(self.__data.loc[:,i].isna())
            print(f"{i} has {x} NaN values")

class visual:
    def __init__(self, data):
        self.__data = data
        import matplotlib.pyplot
        import matplotlib.dates
        self.plt = matplotlib.pyplot
        self.dates = matplotlib.dates

    def timeline(self, x, y, n):
        fig, ax = self.plt.subplots(figsize = (8,5))

        self.plt.plot(self.__data[x], self.__data[y])

        ax.xaxis.set_major_locator(self.dates.MonthLocator())
        ax.xaxis.set_major_formatter(self.dates.DateFormatter('%b %Y'))
        self.plt.setp(ax.get_xticklabels(), rotation=50)

        self.plt.xlabel ('Date')
        self.plt.ylabel (str(y))
        self.plt.title(n)

        self.plt.tight_layout()
        self.plt.show()
