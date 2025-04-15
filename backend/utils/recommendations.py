import pandas as pd


def generate_recommendations(meta_df, shopify_df):
    recommendations = []

    for i in range(len(meta_df)):
        date = meta_df['date'][i]
        ctr = meta_df['ctr'][i]
        spend = meta_df['spend'][i]
        conversions = meta_df['conversions'][i]
        total_sales = shopify_df['total_sales'][i] if i < len(shopify_df) else 0
        roi = total_sales / spend if spend > 0 else 0

        message = f"{date}: "

        if roi < 1.0:
            message += "Low ROI detected. Consider pausing or reducing budget."
        elif roi > 2.0:
            message += "High ROI. You may consider increasing budget here."
        else:
            message += "Average performance. Monitor closely."

        if ctr < 0.02:
            message += " CTR is low. Suggest testing new ad creative (A/B test)."
        elif ctr > 0.05:
            message += " CTR is excellent. Continue with current ad creative."

        if conversions == 0 and spend > 50:
            message += " High spend but no conversions. Strongly consider running A/B test for audience targeting or ad copy."

        recommendations.append(message)

    return recommendations
