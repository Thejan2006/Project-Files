<?php
header('Content-Type: application/json; charset=utf-8');

$start = filter_input(INPUT_POST, 'start', FILTER_VALIDATE_INT);
$end   = filter_input(INPUT_POST, 'end', FILTER_VALIDATE_INT);

if ($start === false || $end === false || $start === null || $end === null) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Invalid input. Provide integer start and end.']);
    exit;
}

// generate inclusive list, support descending ranges
$numbers = [];
if ($start <= $end) {
    for ($i = $start; $i <= $end; $i++) $numbers[] = $i;
} else {
    for ($i = $start; $i >= $end; $i--) $numbers[] = $i;
}

// Try to save to DB (optional). If DB not configured/available, continue without failing.
$dbHost = '127.0.0.1';
$dbName = 'testdb';
$dbUser = 'root';
$dbPass = 'password'; // <- change to your DB password
$dsn = "mysql:host={$dbHost};dbname={$dbName};charset=utf8mb4";

try {
    $pdo = new PDO($dsn, $dbUser, $dbPass, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);

    $stmt = $pdo->prepare('INSERT INTO number_ranges (start_num, end_num, numbers) VALUES (:s, :e, :nums)');
    $stmt->execute([
        ':s' => $start,
        ':e' => $end,
        ':nums' => json_encode($numbers, JSON_UNESCAPED_UNICODE),
    ]);
} catch (PDOException $ex) {
    // If DB fails, we won't return an error to the user — just continue.
    // Optionally log $ex->getMessage() to a file in production.
}

// Return JSON result
echo json_encode(['success' => true, 'numbers' => $numbers]);