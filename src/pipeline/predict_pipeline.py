import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



# class CustomData:
#     def __init__(  self,
#         gender: str,
#         race_ethnicity: str,
#         parental_level_of_education,
#         lunch: str,
#         test_preparation_course: str,
#         reading_score: int,
#         writing_score: int):

#         self.gender = gender

#         self.race_ethnicity = race_ethnicity

#         self.parental_level_of_education = parental_level_of_education

#         self.lunch = lunch

#         self.test_preparation_course = test_preparation_course

#         self.reading_score = reading_score

#         self.writing_score = writing_score

#     def get_data_as_data_frame(self):
#         try:
#             custom_data_input_dict = {
#                 "gender": [self.gender],
#                 "race_ethnicity": [self.race_ethnicity],
#                 "parental_level_of_education": [self.parental_level_of_education],
#                 "lunch": [self.lunch],
#                 "test_preparation_course": [self.test_preparation_course],
#                 "reading_score": [self.reading_score],
#                 "writing_score": [self.writing_score],
#             }

#             return pd.DataFrame(custom_data_input_dict)

#         except Exception as e:
#             raise CustomException(e, sys)

class CustomData:
    def __init__(
        self,

        # Numerical Features
        year: float,
        metacritic_score: float,
        user_score: float,
        critic_review_count: float,
        user_review_count: float,
        na_sales_million: float,
        eu_sales_million: float,
        jp_sales_million: float,
        other_sales_million: float,
        global_sales_million: float,
        estimated_revenue_million_usd: float,
        how_long_to_beat_main_hrs: float,
        launch_price_usd: float,

        # Categorical Features
        platform: str,
        platform_type: str,
        platform_maker: str,
        platform_generation: str,
        genre: str,
        publisher: str,
        developer: str,
        publisher_region: str,
        publisher_tier: str,
        esrb_rating: str,
        is_sequel: str,
        online_multiplayer: str,
        dlc_released: str,
        microtransactions: str,
        loot_boxes: str,
        game_pass_available: str,
        vr_support: str,
        goty_nominated: str,
        goty_won: str

    ):

        # Numerical
        self.year = year
        self.metacritic_score = metacritic_score
        self.user_score = user_score
        self.critic_review_count = critic_review_count
        self.user_review_count = user_review_count
        self.na_sales_million = na_sales_million
        self.eu_sales_million = eu_sales_million
        self.jp_sales_million = jp_sales_million
        self.other_sales_million = other_sales_million
        self.global_sales_million = global_sales_million
        self.estimated_revenue_million_usd = estimated_revenue_million_usd
        self.how_long_to_beat_main_hrs = how_long_to_beat_main_hrs
        self.launch_price_usd = launch_price_usd

        # Categorical
        self.platform = platform
        self.platform_type = platform_type
        self.platform_maker = platform_maker
        self.platform_generation = platform_generation
        self.genre = genre
        self.publisher = publisher
        self.developer = developer
        self.publisher_region = publisher_region
        self.publisher_tier = publisher_tier
        self.esrb_rating = esrb_rating
        self.is_sequel = is_sequel
        self.online_multiplayer = online_multiplayer
        self.dlc_released = dlc_released
        self.microtransactions = microtransactions
        self.loot_boxes = loot_boxes
        self.game_pass_available = game_pass_available
        self.vr_support = vr_support
        self.goty_nominated = goty_nominated
        self.goty_won = goty_won


    def get_data_as_data_frame(self):

        try:

            custom_data_input_dict = {

                # Numerical
                "year":[self.year],
                "metacritic_score":[self.metacritic_score],
                "user_score":[self.user_score],
                "critic_review_count":[self.critic_review_count],
                "user_review_count":[self.user_review_count],
                "na_sales_million":[self.na_sales_million],
                "eu_sales_million":[self.eu_sales_million],
                "jp_sales_million":[self.jp_sales_million],
                "other_sales_million":[self.other_sales_million],
                "global_sales_million":[self.global_sales_million],
                "estimated_revenue_million_usd":[self.estimated_revenue_million_usd],
                "how_long_to_beat_main_hrs":[self.how_long_to_beat_main_hrs],
                "launch_price_usd":[self.launch_price_usd],

                # Categorical
                "platform":[self.platform],
                "platform_type":[self.platform_type],
                "platform_maker":[self.platform_maker],
                "platform_generation":[self.platform_generation],
                "genre":[self.genre],
                "publisher":[self.publisher],
                "developer":[self.developer],
                "publisher_region":[self.publisher_region],
                "publisher_tier":[self.publisher_tier],
                "esrb_rating":[self.esrb_rating],
                "is_sequel":[self.is_sequel],
                "online_multiplayer":[self.online_multiplayer],
                "dlc_released":[self.dlc_released],
                "microtransactions":[self.microtransactions],
                "loot_boxes":[self.loot_boxes],
                "game_pass_available":[self.game_pass_available],
                "vr_support":[self.vr_support],
                "goty_nominated":[self.goty_nominated],
                "goty_won":[self.goty_won]

            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e,sys)