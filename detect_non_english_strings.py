# Detect non-english strings in title and remove them from df_details:

# Set display option so that we can see all rows because we will likely manually review the values:
pd.set_option('display.max_rows', df_details.shape[0]+1)

# Create function to detect non-english strings:


def detect_en(ascii_string):
    try:
        ascii_string.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


column_names = ["id", "title"]
flag_non_en = pd.DataFrame(columns=column_names)
for item in df_details.loc[:, 'title']:
    if isEnglish(item) == False:
        flag_non_en = flag_non_en.append(
            df_details[['id', 'title']].loc[df_details['title'] == item])
# print(flag_non_en)
