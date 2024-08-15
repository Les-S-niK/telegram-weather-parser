
## Built-in modules
from requests import get
from requests import ConnectionError, Response

## Pip modules
from bs4 import BeautifulSoup, element
from fake_headers import Headers


class WeatherParser(object):
    """Weather parser class. You can get the information 
    about weather in your city.

    Args:
        object : Basic inheritance class in Python3.
    """
    def __init__(
        self,
        country: str,
        city: str
    ) -> None:
        """initialization WeatherParser class.
        You need to give args <county> and <city>.

        Args:
            country (str): Country for parse weather.
            city (str): City in this county for parse weather.
        """
        ## City name for parsing.
        self.CITY : str = city.lower()
        ## County name for parsing.
        self.COUNTRY: str = country.lower()
        ## Site url for parsing.
        self.URL: str = f"https://world-weather.ru/pogoda/{country}/{city}/"
        ## Headers for parsing.
        self.headers: dict = self._generate_headers()
        ## Response from site URL.
        self._response: Response = self._fetch_weather_data()
        ## HTML markup.
        self._soup: BeautifulSoup = self._get_html()
        ## Weather information.
        self._weather_info: list = self._parse_html()
        ## Structured in-dictionary weather information.
        self.weather_information: dict = self.__structure_parsed_values()
        
        return None
    
    
    def create_html_file(
        self,
        filename: str = "index.html"
    ) -> None:
        """Create .HTML file for debugging and read the markup.

        Args:
            filename (str, optional): Filename to create. Defaults to "index.html".
        """
        ## Check if filename has .html.
        if not filename.endswith(".html"):
            filename = f"{filename}.html"
        
        ## Open the file.
        with open(
            file=filename,
            mode="w",
            encoding="utf-8"
        ) as file:
            ## Write the HTML markup.
            file.write(str(self._soup))
        
        return None
    
    
    def _parse_html(self) -> list:
        """Parse HTML markup from soup object.

        Returns:
            dict: dictionary with structured information
        """
        DIV_ID_NAME: str = "weather-now-description"
        ## Get <div> with weather description.
        weather_now_description_div: element.Tag = self._soup.find(
            "div",
            id=DIV_ID_NAME
        )
        ## Get <dl> tag for get weather.
        weather_now: element.Tag = weather_now_description_div.find("dl")
        ## Find all <dd> tags with information about weather.
        all_dd_tags: list = weather_now.find_all("dd")
        
        ## Return parsed values. 
        return all_dd_tags
    
    
    def _get_html(self) -> BeautifulSoup:
        """Get instanse of class BeautifulSoup.

        Returns:
            BeautifulSoup: Html markup.
        """
        ## Get soup.
        soup: BeautifulSoup = BeautifulSoup(
            markup=self._response.content,
            features="lxml"
        )
        
        return soup
    
    
    def _fetch_weather_data(self) -> Response:
        """Get response from site for parsing it by BeautifulSoup4.

        Returns:
            Response: request.Response class instanse. 
        """
        ## Response to GET. 
        response: Response = get(
            url=self.URL,
            headers=self.headers
        )
        
        ## Check if response has a good status.
        if response.ok:
            return response
        else:
            raise ConnectionError(f"""
                Connection error. Status code: {response.status_code}.
                URL: {self.URL}. 
                """,
                response=response
            )


    def __structure_parsed_values(self) -> dict:
        """Structuring parsed weather values and return it in dictionary.

        Returns:
            dict: Structured parsed values.
        """
        ## Create empty dictionary for add a new values inside it.
        weather_info: dict = {}
        ## Create list of elements name to add it in dictionary.
        elements_name: list = [
            "temp",
            "pressure",
            "humidity",
            "wind",
            "max_wind",
            "cloudness",
            "visibility",
            "uv_index"
        ]
        ## Create a <info> var for type annotation.
        info: element.Tag = None
        
        ## Use <for> loop for concatinate elements in dictionary.
        for info, element_name, element_number \
        in zip(self._weather_info, elements_name, range(len(self._weather_info))):
            ELEMENT_NUMBER_TO_REPLACE: int = 3
            ## If element number equals 3, skip it.
            if element_number == ELEMENT_NUMBER_TO_REPLACE:
                continue
            
            ## Add values to dictionary.
            weather_info[element_name] = info.text
        
        ## Replace russ. letters to engl. in pressure
        pressure: str = weather_info.get("pressure")
        pressure = pressure.replace("мм рт. ст.", "mm of merc.")
        ## re-write pressure.
        weather_info["pressure"] = pressure
        
        ## Replace russ. letters to engl. in max_wind speed
        max_wind: str = weather_info.get("max_wind")
        max_wind = max_wind.replace("м/с", "mp/s")
        ## re-write pressure.
        weather_info["max_wind"] = max_wind
        
        ## Return structured information.
        return weather_info


    @staticmethod
    def _generate_headers() -> dict:
        """Generate headers for parsing Weather.

        Returns:
            dict: Header for parsing."""
        ## Create instance of class Headers for headers generation.
        headers: Headers = Headers(
            headers=True
        )
        ## Generate random headers and return it.
        return headers.generate()


if __name__ == "__main__":
    weather = WeatherParser(
        country="russia",
        city="sochi"
    )
    print(weather.weather_information)