# rule 01 skip-string-normalization

## 01 preserve single or triple quote
singlequote = 'This is single quote'

triplequote = '''This is triple quote'''

greeting = f'Hello, {name}!'


## 02 preserve unicode prefix

uprefix = u'Hello,World'

## 03 preserve raw string :backslashes are treated as literal characters and not as escape sequences.

pattern = r'\d+'

# rule 02 skip-magic-trailing-comma

skip_trailing_coma = [1, 2, 3]  # ← empty not comma
preserve_multiline = [
    1,
    2,
    3,  # ← this comma is "magic" dont skip
]


# rule 03 line-length = 88


# long function args line
def long_func_args(
    argument1, argument2, argument3, argument4, argument5, argument6
):
    pass


# long list values
long_list = [
    1,
    "One Number",
    2,
    "Two Number",
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    "Ten Number",
]


# long dict key : (value)

settings = {
    "this_is_a_very_long_key_name": (
        "this_is_a_very_long_value_that_needs_wrapping_due_to_length_limit_"
    ),
}


# chaining methods calls:

data = (
    my_dataframe.sort_values("name")
    .drop_duplicates()
    .reset_index(drop=True)
)


# for 'long text...' not apply rule :
long_text_ = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'
