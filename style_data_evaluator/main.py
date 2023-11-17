import pandas as pd
import os

root_path = 'second_bucket'
list_ = os.listdir(root_path)

for i in list_:
    path = os.path.join(root_path,i)
    # Load the main_df file
    main_df = pd.read_csv("main_df.csv")

    # Load the first_tag file
    first_tag = pd.read_csv(os.path.join(path, "first_tag.csv"))

    # Load the second_tag file
    second_tag = pd.read_csv(os.path.join(path, "output.csv"))

    # Merge main_df with first_tag on Old_Name column
    merged_df = pd.merge(main_df, first_tag, left_on="Old_Name", right_on="Name", how="left")

    # Merge merged_df with second_tag on New_Name column
    merged_df = pd.merge(merged_df, second_tag, left_on="New_Name", right_on="Name", how="left")

    # Create a new dataframe to store the results
    results_df = pd.DataFrame(columns=["New_Name", "Old_Name", "Status_first_tag", "Status_second_tag", "Validity"])

    # Loop through main_df and fill in the results dataframe
    for index, row in main_df.iterrows():
        new_name = row["New_Name"]
        old_name = row["Old_Name"]
        status_first_tag = merged_df.loc[merged_df["Old_Name"] == old_name, "Status_x"].iloc[0] if old_name in \
                                                                                                   merged_df[
                                                                                                       "Old_Name"].values else 'None'
        status_second_tag = merged_df.loc[merged_df["New_Name"] == new_name, "Status_y"].iloc[0] if new_name in \
                                                                                                    merged_df[
                                                                                                        "New_Name"].values else 'None'
        if pd.isna(status_first_tag) or pd.isna(status_second_tag):
            validity = "-"
        elif status_first_tag == status_second_tag:
            validity = "valid"
        else:
            validity = "not-valid"
        # results_df = results_df.append(
        #     {"New_Name": new_name, "Old_Name": old_name, "Status_first_tag": status_first_tag,
        #      "Status_second_tag": status_second_tag, "Validity": validity}, ignore_index=True)

        results_df = pd.concat([results_df, pd.DataFrame({"New_Name": [new_name], "Old_Name": [old_name],
                                                          "Status_first_tag": [status_first_tag],
                                                          "Status_second_tag": [status_second_tag],
                                                          "Validity": [validity]})], ignore_index=True)

    result_path = os.path.join(path,"results.csv")
    # Save the results dataframe to a new csv file
    results_df.to_csv(result_path, index=False)
