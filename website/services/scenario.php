<?php
include('config.php');

$lexp = $_POST['lexp'];
$temp = $_POST['temperature'];
$model = $_POST['model'];

$messages = [
    [
        'role' => "user",
        'content'=> 'Does the following passage help address and answer the scenario described below?
        Give me the answer as a JSON structure with two keys: \'childhood\' and \'reason\'. The attribute 
        of \'childhood\' should either be true or false to indicate your answer and the attribute of \'reason\' should 
        be the reasons for you answer. Please do not include any artifacts for formatting. 
        Just give me the JSON object and nothing else.'
    ],
    [
        'role' => "user",
        'content'=> 'Scenario: Ortenz wants to characterize children’s experience of music as witnessed in bibliographic 
               and artistic sources. She is looking for primary sources (e.g. Personal journals, literary texts) 
               wherein to find evidence of listening experiences. She needs to collect and analyze large corpora 
               of texts and images recording or depicting children’s experience with music. Documents include 
               official sources (e.g. newspaper articles, reviews of concerts, paintings) and sources produced by \'odinary people\'. 
               She prefers the latter as they provide more reliable feedback, and she looks at the context of 
               production of such sources (where, when, who created the source, the goal, which related events exist), 
               contents (recurring motifs and themes), and elicited emotional responses. She collects sources 
               belonging to different historical periods so as to characterize the development of identified phenomena.'
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
