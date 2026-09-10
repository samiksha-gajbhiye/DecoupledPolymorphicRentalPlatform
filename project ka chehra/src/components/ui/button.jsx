import * as React from "react";
import { Slot } from "@radix-ui/react-slot";

const Button = React.forwardRef(
  ({ className, variant = "default", children, asChild = false, ...props }, ref
) => {
  const Comp = asChild ? "span" : "button";
  return (
    <Comp
      ref={ref}
      className={className}
      {...props}
    >
      {children}
    </Comp>
  );
});
Button.displayName = "Button";

export { Button };