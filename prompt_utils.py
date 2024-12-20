
def construct_prompt(text, task, modal='multi'):
    
    if task == "sentiment_analysis":
        if modal == 'multi':
            prompt = f"""
            This image has the caption: "{text}".  
            What sentiment does this combination convey? 
            Choose only 'positive', 'neutral' or 'negative' as the answer.
            Respond in JSON format, using the following structure:

            ## Example Output
            {{
            "Label": ...
            }}
            """
        elif modal == 'uni':
            prompt = f"""
            What sentiment does this post convey? 
            Post: "{text}"
            Choose only 'positive', 'neutral' or 'negative' as the answer.
            Respond in JSON format, using the following structure:

            ## Example Output
            {{
            "Label": ...
            }}
            """
    elif task == "hate_speech_detection":
        if modal == 'multi':
            prompt = f"""
            Is this image hateful or non-hateful?  
            Choose only 'hateful' or 'non-hateful' as the answer.
            Respond in JSON format, using the following structure:

            ## Example Output
            {{
            "Label": ...
            }}
            """
        elif modal == 'uni':
            prompt = f"""
            Is this post hateful or non-hateful?  
            Post: "{text}"
            Choose only 'hateful' or 'non-hateful' as the answer.
            Respond in JSON format, using the following structure:

            ## Example Output
            {{
            "Label": ...
            }}
            """
    elif task == "fake_news_identification":
        if modal == 'multi':
            prompt = f"""
            This news article, "{text}", is associated with this image.
            Is this news fake or real?
            Choose only 'fake' or 'real' as the answer.
            Respond in JSON format, using the following structure:

            ## Example Output
            {{
            "Label": ...
            }}
            """
        elif modal == 'uni':
            prompt = f"""
            Is this news article fake or real?
            News: "{text}"
            Choose only 'fake' or 'real' as the answer.
            Respond in JSON format, using the following structure:

            ## Example Output
            {{
            "Label": ...
            }}
            """
    elif task == "demographic_inference":
        if modal == 'multi':
            prompt = f"""
            Based on the images and captions posted by this user (captions: {text}), is the user more likely to be a male or a female?
            Choose only 'male' or 'female' as the answer.
            Respond in JSON format, using the following structure:

            ## Example Output
            {{
            "Label": ...
            }}
            """
        elif modal == 'uni':
            prompt = f"""
            Based on the posts made by this user (posts: {text}), is the user more likely to be a male or a female?
            Choose only 'male' or 'female' as the answer.
            Respond in JSON format, using the following structure:

            ## Example Output
            {{
            "Label": ...
            }}
            """
    elif task == "ideology_detection":
        if modal == "multi":
            prompt = f"""
            The following image is paired with this caption: '{text}'. Based on this image and caption, what is the likely ideology of the author?
            Choose only 'left', 'center' or 'right' as the answer.
            Respond in JSON format, using the following structure:

            ## Example Output
            {{
            "Label": ...
            }}
            """
        elif modal == "uni":
            prompt = f"""
            Based on this post, what is the likely ideology of the author?
            Post: "{text}"
            Choose only 'left', 'center' or 'right' as the answer.
            Respond in JSON format, using the following structure:

            ## Example Output
            {{
            "Label": ...
            }}
            """

    return prompt