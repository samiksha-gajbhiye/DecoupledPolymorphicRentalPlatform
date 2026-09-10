import * as React from "react";
import { Checkbox as PrimitiveCheckbox } from "@radix-ui/react-checkbox";

const Checkbox = React.forwardRef(
  ({ className, ...props }, ref) => (
    <PrimitiveCheckbox
      ref={ref}
      className={className}
      {...props}
    />
  )
);
Checkbox.displayName = PrimitiveCheckbox.displayName;

export { Checkbox };