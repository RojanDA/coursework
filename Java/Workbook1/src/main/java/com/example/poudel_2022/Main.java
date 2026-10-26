package com.example.poudel_1002238306;

public class Main {
    public static void main(String[] args) {
        System.out.println("Starting Producer-Consumer Simulation with ReentrantLock");
        System.out.println("======================================================");

        // Create shared buffer
        SharedBuffer buffer = new SharedBuffer();

        // Define colors for each thread
        String producerColor = ColorUtil.GREEN;
        String[] consumerColors = {
                ColorUtil.BLUE,
                ColorUtil.RED,
                ColorUtil.CYAN
        };

        // Create and start producer thread
        Thread producerThread = new Thread(new Producer(buffer, producerColor));

        // Create and start three consumer threads
        Thread[] consumerThreads = new Thread[3];
        for (int i = 0; i < 3; i++) {
            consumerThreads[i] = new Thread(new Consumer(buffer, i + 1, consumerColors[i]));
        }

        // Start all threads
        producerThread.start();
        for (Thread consumerThread : consumerThreads) {
            consumerThread.start();
        }

        // Wait for all threads to complete
        try {
            producerThread.join();
            for (Thread consumerThread : consumerThreads) {
                consumerThread.join();
            }

            System.out.println("\n======================================================");
            System.out.println("All threads have completed execution.");
            System.out.println("Simulation finished successfully!");

        } catch (InterruptedException e) {
            System.out.println("Main thread was interrupted.");
            Thread.currentThread().interrupt();
        }
    }
}