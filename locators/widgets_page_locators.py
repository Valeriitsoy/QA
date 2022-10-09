from selenium.webdriver.common.by import By


class AccordionPageLocators:

    SECTION_1 = (By.CSS_SELECTOR, "div[id='section1Heading']")
    SECTION_2 = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECTION_3 = (By.CSS_SELECTOR, "div[id='section3Heading']")

    SECTION_1_CONTENT = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    SECTION_2_CONTENT = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    SECTION_3_CONTENT = (By.CSS_SELECTOR, "div[id='section3Content'] p")


class AutoCompletePageLocators:

    MULTI_COMPLETE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTI_VALUE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value']")
    MULTI_VALUE_TEXT = (By.CSS_SELECTOR, "div[id='autoCompleteMultipleContainer']")
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path")
    MULTI_VALUE_REMOVE_ALL = (By.CSS_SELECTOR, "div[class='auto-complete__indicators css-1wy0on6'] svg path")
    SINGLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")
    SINGLE_VALUE = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")


class DatePickerPageLocators:

    DATE_INPUT = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

    DATE_TIME_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    DATE_TIME_MONTH = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
    DATE_TIME_YEAR = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
    DATE_TIME_TIME_LIST = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")
    DATE_TIME_MONTH_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
    DATE_TIME_YEAR_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")


class SliderPageLocators:

    INPUT_SLIDER = (By.CSS_SELECTOR, "input[class='range-slider range-slider--primary']")
    SLIDER_VALUE = (By.CSS_SELECTOR, "input[id='sliderValue']")


class ProgressBarPageLocators:

    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, "button[id='startStopButton']")
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")


class TabsPageLocators:

    TABS_WHAT = (By.CSS_SELECTOR, "a[id='demo-tab-what']")
    TABS_WHAT_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-what']")
    TABS_ORIGIN = (By.CSS_SELECTOR, "a[id='demo-tab-origin']")
    TABS_ORIGIN_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-origin']")
    TABS_USE = (By.CSS_SELECTOR, "a[id='demo-tab-use']")
    TABS_USE_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-use']")
    TABS_MORE = (By.CSS_SELECTOR, "a[id='demo-tab-more']")
    TABS_MORE_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-more']")


class ToolTipsPageLocators:

    BUTTON = (By.CSS_SELECTOR, "button[id='toolTipButton']")
    INPUT = (By.CSS_SELECTOR, "input[id='toolTipTextField']")
    CONTRARY_LINK = (By.XPATH, "//*[.='Contrary']")
    SECTION_LINK = (By.XPATH, "//*[.='1.10.32']")

    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, "button[aria-describedby='buttonToolTip']")
    TOOL_TIP_FIELD = (By.CSS_SELECTOR, "input[aria-describedby='textFieldToolTip']")
    TOOL_TIP_CONTRARY_LINK = (By.CSS_SELECTOR, "a[aria-describedby='contraryTexToolTip']")
    TOOL_TIP_SECTION_LINK = (By.CSS_SELECTOR, "a[aria-describedby='sectionToolTip']")
    TOOL_TIP_INNERS = (By.CSS_SELECTOR, "div[class='tooltip-inner']")

