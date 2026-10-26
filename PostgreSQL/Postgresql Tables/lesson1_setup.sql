-- ============================================================
-- LESSON 1: Full Query Structure & GROUP BY Reflex
-- Phase 1, Day 1 — 30-Day SQL Mentoring Programme
-- Database: PostgreSQL
-- ============================================================

-- ============================================================
-- STEP 0: Set up the practice database
-- Run this entire script in your PostgreSQL environment
-- (psql, pgAdmin, DBeaver, or any PostgreSQL client)
-- ============================================================

-- Create the practice database (run this first, then connect to it)
-- CREATE DATABASE sql_mentoring;
-- \c sql_mentoring  -- connect to it

-- Drop tables if they exist (for clean re-runs)
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS merchants;

-- ============================================================
-- USERS table
-- ============================================================
CREATE TABLE users (
    user_id      SERIAL PRIMARY KEY,
    user_name    VARCHAR(100) NOT NULL,
    city         VARCHAR(50),
    email        VARCHAR(150),
    signup_date  DATE NOT NULL DEFAULT CURRENT_DATE
);

-- ============================================================
-- MERCHANTS table
-- ============================================================
CREATE TABLE merchants (
    merchant_id   SERIAL PRIMARY KEY,
    merchant_name VARCHAR(100) NOT NULL,
    category      VARCHAR(50),
    city          VARCHAR(50)
);

-- ============================================================
-- TRANSACTIONS table
-- ============================================================
CREATE TABLE transactions (
    txn_id       SERIAL PRIMARY KEY,
    user_id      INTEGER REFERENCES users(user_id),
    merchant_id  INTEGER REFERENCES merchants(merchant_id),
    amount       NUMERIC(10, 2),
    status       VARCHAR(20),
    created_at   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- INSERT SAMPLE DATA
-- ============================================================

-- Users
INSERT INTO users (user_name, city, email, signup_date) VALUES
('Alice Sharma',   'Kathmandu', 'alice@example.com',  '2025-01-15'),
('Bishal Thapa',   'Pokhara',   'bishal@example.com','2025-02-20'),
('Sita Gurung',    'Lalitpur',  'sita@example.com',  '2025-03-10'),
('Ram Maharjan',   'Bhaktapur', 'ram@example.com',   '2025-03-25'),
('Gita Rai',       'Kathmandu', 'gita@example.com',  '2025-04-01'),
('Hari Adhikari',  'Pokhara',   'hari@example.com',  '2025-04-15'),
('Maya Tamang',    'Lalitpur',  'maya@example.com',   '2025-05-05'),
('Kiran KC',      'Kathmandu', 'kiran@example.com',  '2025-05-20');

-- Merchants
INSERT INTO merchants (merchant_name, category, city) VALUES
('eSewa Mart',         'E-commerce',  'Kathmandu'),
('Daraz Express',      'E-commerce',  'Lalitpur'),
('Bhatbhateni Super',  'Grocery',     'Kathmandu'),
('Foodmandu',           'Food',        'Kathmandu'),
('Pathao Pay',          'Digital Pay', 'Pokhara'),
('Goldstar Shoes',      'Retail',      'Bhaktapur'),
('Himalaya Bank',       'Banking',     'Kathmandu'),
('OnlineBhet',          'E-commerce',  'Pokhara');

-- Transactions (deliberately includes: NULL amounts, NULL statuses,
-- multiple statuses: 'success', 'failed', 'pending', 'refunded'
-- different merchants, different dates across months)
INSERT INTO transactions (user_id, merchant_id, amount, status, created_at) VALUES
(1, 1, 2500.00, 'success',  '2025-06-01 10:30:00'),
(1, 3, 1200.00, 'success',  '2025-06-05 14:20:00'),
(1, 4, 800.00,  'failed',   '2025-06-10 09:15:00'),
(2, 2, 3000.00, 'success',  '2025-06-03 16:45:00'),
(2, 5, NULL,    'pending',  '2025-06-08 11:00:00'),
(3, 1, 1500.00, 'success',  '2025-06-02 13:10:00'),
(3, 6, 4500.00, 'success',  '2025-06-07 15:30:00'),
(3, 7, 2000.00, 'failed',   '2025-06-12 10:00:00'),
(4, 8, 750.00,  'success',  '2025-06-04 12:00:00'),
(4, 3, NULL,    'failed',   '2025-06-09 17:30:00'),
(5, 1, 3200.00, 'success',  '2025-06-06 14:15:00'),
(5, 2, 1000.00, 'pending', '2025-06-11 08:45:00'),
(6, 5, 1800.00, 'success',  '2025-06-05 10:30:00'),
(6, 4, 500.00,  'refunded', '2025-06-10 19:00:00'),
(7, 7, 5000.00, 'success',  '2025-06-08 11:30:00'),
(7, 1, 900.00,  'success',  '2025-06-13 14:00:00'),
(8, 2, 2100.00, 'success',  '2025-06-04 16:20:00'),
(8, 6, NULL,    'pending',  '2025-06-09 09:45:00'),
(1, 2, 600.00,  'success',  '2025-07-01 10:00:00'),
(2, 1, 1700.00, 'success',  '2025-07-03 13:30:00'),
(3, 4, 400.00,  'failed',   '2025-07-05 15:00:00'),
(4, 5, 2800.00, 'success',  '2025-07-07 11:15:00'),
(5, 3, 950.00,  'success',  '2025-07-10 14:45:00'),
(6, 8, 1100.00, 'success',  '2025-07-12 16:00:00'),
(7, 2, 3300.00, 'success',  '2025-07-15 10:30:00'),
(8, 7, NULL,    'failed',   '2025-07-18 09:00:00');

-- ============================================================
-- VERIFICATION: Check what's in the tables
-- ============================================================
-- Run these to confirm your data loaded correctly:

-- SELECT COUNT(*) FROM users;        -- should return 8
-- SELECT COUNT(*) FROM merchants;    -- should return 8
-- SELECT COUNT(*) FROM transactions; -- should return 26

-- Check the actual status values (this is your FIRST habit!)
-- SELECT DISTINCT status FROM transactions;
-- Expected: success, failed, pending, refunded

-- Check for NULLs (your SECOND habit!)
-- SELECT COUNT(*) FROM transactions WHERE amount IS NULL;
-- Expected: 4

-- ============================================================
-- END OF SETUP
-- ============================================================
