class ContactPipeline:
    def process_item(self, item, spider):
        # Clean and validate the scraped item
        if self.validate_item(item):
            # Here you can add code to store the item, e.g., in a database
            return item
        else:
            raise DropItem("Invalid item found: %s" % item)

    def validate_item(self, item):
        # Implement validation logic for the scraped item
        return all([item.get('name'), item.get('email'), item.get('phone')])  # Example validation

    def close_spider(self, spider):
        # Perform any cleanup actions when the spider closes
        pass