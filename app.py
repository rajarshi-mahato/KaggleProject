from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method == 'GET':

        return render_template('home.html')

    else:

        data = CustomData(

            # Numerical Features

            year=float(request.form.get("year")),

            metacritic_score=float(
                request.form.get("metacritic_score")
            ),

            user_score=float(
                request.form.get("user_score")
            ),

            critic_review_count=float(
                request.form.get("critic_review_count")
            ),

            user_review_count=float(
                request.form.get("user_review_count")
            ),

            na_sales_million=float(
                request.form.get("na_sales_million")
            ),

            eu_sales_million=float(
                request.form.get("eu_sales_million")
            ),

            jp_sales_million=float(
                request.form.get("jp_sales_million")
            ),

            other_sales_million=float(
                request.form.get("other_sales_million")
            ),

            global_sales_million=float(
                request.form.get("global_sales_million")
            ),

            estimated_revenue_million_usd=float(
                request.form.get(
                    "estimated_revenue_million_usd"
                )
            ),

            how_long_to_beat_main_hrs=float(
                request.form.get(
                    "how_long_to_beat_main_hrs"
                )
            ),

            launch_price_usd=float(
                request.form.get(
                    "launch_price_usd"
                )
            ),

            # Categorical Features

            platform=request.form.get("platform"),

            platform_type=request.form.get(
                "platform_type"
            ),

            platform_maker=request.form.get(
                "platform_maker"
            ),

            platform_generation=request.form.get(
                "platform_generation"
            ),

            genre=request.form.get(
                "genre"
            ),

            publisher=request.form.get(
                "publisher"
            ),

            developer=request.form.get(
                "developer"
            ),

            publisher_region=request.form.get(
                "publisher_region"
            ),

            publisher_tier=request.form.get(
                "publisher_tier"
            ),

            esrb_rating=request.form.get(
                "esrb_rating"
            ),

            is_sequel=request.form.get(
                "is_sequel"
            ),

            online_multiplayer=request.form.get(
                "online_multiplayer"
            ),

            dlc_released=request.form.get(
                "dlc_released"
            ),

            microtransactions=request.form.get(
                "microtransactions"
            ),

            loot_boxes=request.form.get(
                "loot_boxes"
            ),

            game_pass_available=request.form.get(
                "game_pass_available"
            ),

            vr_support=request.form.get(
                "vr_support"
            ),

            goty_nominated=request.form.get(
                "goty_nominated"
            ),

            goty_won=request.form.get(
                "goty_won"
            )
        )

        pred_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()

        results = predict_pipeline.predict(
            pred_df
        )

        return render_template(
            'home.html',
            results=round(results[0],2)
        )


if __name__ == "__main__":

   app.run(debug=True, host="0.0.0.0", port=5000)