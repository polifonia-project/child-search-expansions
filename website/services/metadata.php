<?php
include('config.php');

$lexp = $_POST['lexp'];
$temp = $_POST['temperature'];
$model = $_POST['model'];

$messages = [
    [
        'role' => "user",
        'content'=> "'Listeners': Please enter the full name of the listener or listeners without any additional text. It must be a persons' name. If the name is in
        Pronoun form (such as 'I', 'He', 'She'), is used, use the listeners name.
        'Listening to': Please specify only the title or name of what is being listening to, without any extra details.
        'Performed by': Mention who performed or delivered the content being listened to.
        'Date/Time': Extract all date and time in whatever format they appear in the provided text.
        then, you must convert the date and time to UTC in the
        format 'YYYY-MM-DDTHH:MM:SSZ'. If Month, Day, time (Hour, Minutes, Seconds) are missing
        in the text, use '00' for them.
        'Medium': Choose one from - 'Live', 'Playback', 'Broadcast', or 'Others'. Choose Live, if the context relates to live music performances
        where the listener is present at the venues or events such as: Concerts, Theatres, Parks, Clubs, Bars,
        Street Performances, House Concerts, Stadiums, Coffee Shops, Churches, Cathedrals, Open Mics, Radio Shows,
        or TV Shows. Choose Playback, if the text relates to any of the following and is not associated with live
        music performances: Album, MP3, Vinyl, CD, Tapes, 8-Track Tapes, Digital Downloads, FLAC, Radio (for prerecorded music),
        Music Videos, Podcasts (music-focused, on-demand), Satellite Radio, WAV, Streaming (e.g., Spotify, Apple Music),
        Bluetooth Speakers, or Wireless Headphones. Choose Broadcast, if the text relates to any of the following methods or
        platforms for disseminating music, regardless of whether the music is live or pre-recorded such as: Radio
        (AM, FM, Shortwave), Television, Music TV channels, Talent shows, Award ceremonies, Internet Radio, Satellite Radio,
        Podcasts (for music distribution), Webcasts, Live Streaming Platforms, Public Address Systems, or DAB (Digital Audio Broadcasting).
        Choose Others, If the text does not fit the above categories.
        'Listening Environment': Select all the listening environment that applied to the excerpt from the
        following - 'Indoors', 'In the company of others', 'In Public', 'In Private', 'Solitary', 'Outdoors',
        'Domestic', 'Accompanied', or 'Others'. Select Indoors, if the environment is Home, office, commercial
        places (e.g., malls, restaurants), public facilities (e.g., libraries, train stations). Select Outdoors, if
        the environment is Parks, streets, beaches, wilderness (e.g., forests, mountains). Select Solitary, if the
        listener was Alone in the environment, without any other human presence. Select In the Company of Others, if the listener
        was Listening with family, friends, colleagues, or strangers. Select 'In Private', if the Listening happened in private places,
        like personal homes or offices. Select 'In Public', if the environment is an Area with multiple people and reduced privacy.
        Select Domestic, if the listener Listened within household settings, which might include living rooms, bedrooms, or
        kitchens. Select 'Accompanied', if the listener was Listening with one or more individuals, regardless of the
        relationship or setting. Select 'Others', if the listening environment did not fit any of the above categories.
        'Location': Provide the city and country."
    ],
    [
        'role' => "user",
        'content'=> "Act as a knowledge engineer with over 25 years of experience in information extraction,
        analyze the passage below and determine any encounters depicted within it. Please provide a concise answer.
        Respond using a JSON structure with the seven keys described in the custom template above."
    ],
    [
        'role' => "user",
        'content'=> 'Passage: '.$lexp
    ]
];
// The data you want to send via POST
$fields = [
    //'model' => 'gpt-4-turbo', // Specify the model
    'model' => 'gpt-3.5-turbo-0125', // Specify the model
    //'model' => $model,
    'temperature' => (float)$temp,
    'messages' => $messages,
    'max_tokens' => 1024 // Maximum number of tokens to generate
];

// URL for the OpenAI API
$url = 'https://api.openai.com/v1/chat/completions';

// Open connection
$ch = curl_init();

// Set the url, number of POST vars, POST data
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($fields));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer '.$apiKey
]);

// Execute post
$result = curl_exec($ch);
if (curl_errno($ch)) {
    echo 'Error:' . curl_error($ch);
} else {
    // Print the response if you want to debug
    header('Content-Type: application/json; charset=utf-8');
    echo $result;
}

// Close connection
curl_close($ch);
?>
