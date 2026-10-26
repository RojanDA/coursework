package com.example.poudel_1002238306;

public class Consumer implements Runnable {
    private final SharedBuffer buffer;
    private final String color;
    private final int consumerId;

    public Consumer(SharedBuffer buffer, int consumerId, String color) {
        this.buffer = buffer;
        this.consumerId = consumerId;
        this.color = color;
    }

    private String reverseString(String str) {
        return new StringBuilder(str).reverse().toString();
    }

    @Override
    public void run() {
        try {
            while (!buffer.isProductionComplete() || !buffer.isEmpty()) {
                String item = buffer.remove();

                if (item != null) {
                    // Process the string
                    int length = item.length();
                    String reversed = reverseString(item);

                    // Display results with color
                    String message = String.format("CONSUMER-%d: Original='%s', Length=%d, Reversed='%s'",
                            consumerId, item, length, reversed);
                    System.out.println(ColorUtil.colorize(message, color));

                    // Simulate processing time
                    Thread.sleep(300);
                } else {
                    // Buffer is empty but production might not be complete
                    Thread.sleep(100);
                }
            }

            System.out.println(ColorUtil.colorize(
                    String.format("CONSUMER-%d: No more items to process. Exiting.", consumerId), color));

        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.out.println(ColorUtil.colorize(
                    String.format("CONSUMER-%d: was interrupted.", consumerId), color));
        }
    }
}