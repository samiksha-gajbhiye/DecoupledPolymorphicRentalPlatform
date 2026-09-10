import * as React from "react";
import { Slot } from "@radix-ui/react-slot";

const Input = React.forwardRef(({ className, ...props }, ref) => (
  <input
    ref={ref}
 className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-transparent file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50[&::-webkit-outer-spin-button]:m-0[&::-webkit-inner-spin-button]:m-0"
    {...props}
  />
));
Input.displayName = "Input";

export { Input };