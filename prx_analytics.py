import requests
import pandas as pd

class PRXAnalytics:
    def __init__(self):
        # จำลองชุดข้อมูลสถิติแมตช์รอบชิงชนะเลิศของ Paper Rex
        self.mock_match_data = [
            {"Map": "Bind", "Agent_Comp": "Raze, Yoru, Viper, Skye, Astra", "First_Kills": 18, "Clutch_Rounds": 4, "Result": "Win", "Win_Rate": 78.5},
            {"Map": "Sunset", "Agent_Comp": "Neon, Breach, Sova, Cypher, Omen", "First_Kills": 22, "Clutch_Rounds": 6, "Result": "Win", "Win_Rate": 83.3},
            {"Map": "Lotus", "Agent_Comp": "Raze, Fade, Omen, Killjoy, Viper", "First_Kills": 14, "Clutch_Rounds": 2, "Result": "Loss", "Win_Rate": 45.0},
            {"Map": "Breeze", "Agent_Comp": "Yoru, Jett, Sova, Viper, Cypher", "First_Kills": 19, "Clutch_Rounds": 5, "Result": "Win", "Win_Rate": 71.4},
        ]

    def get_summary_dataframe(self):
        """แปลงข้อมูลเป็น Pandas DataFrame เพื่อนำไปวิเคราะห์"""
        df = pd.DataFrame(self.mock_match_data)
        return df

    def calculate_w_gaming_index(self, df):
        """คำนวณดัชนีความดุดัน (W-Gaming Score) จากสถิติ First Kills"""
        avg_fk = df['First_Kills'].mean()
        w_score = min(100, int((avg_fk / 25.0) * 100))
        return w_score
