package com.example.poudel_1002238306;

public class Producer implements Runnable {
    private final SharedBuffer buffer;
    private final String color;

    // Hardcoded strings as required
    private final String[] strings = {
            "Hello", "Multithreading", "Java", "Programming",
            "Synchronization", "ReentrantLock", "Producer",
            "Consumer", "Buffer", "Hello World"
    };

    public Producer(SharedBuffer buffer, String color) {
        this.buffer = buffer;
        this.color = color;
    }

    @Override
    public void run() {
        try {
            for (String str : strings) {
                // Add string to buffer
                buffer.add(str);

                // Print production message with color
                String message = String.format("PRODUCER: Added '%s' to buffer. Buffer size: %d",
                        str, buffer.size());
                System.out.println(ColorUtil.colorize(message, color));

                // Simulate some production time
                Thread.sleep(500);
            }

            // Signal that production is complete
            buffer.setProductionComplete();
            System.out.println(ColorUtil.colorize("PRODUCER: Finished producing all strings.", color));

        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.out.println(ColorUtil.colorize("PRODUCER: was interrupted.", color));
        }
    }
}